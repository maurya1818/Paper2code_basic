import React, { useState } from 'react';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [activeTab, setActiveTab] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setStatus('');
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setStatus('Please select a PDF file first.');
      return;
    }

    setLoading(true);
    setStatus('Processing PDF and generating code... This may take up to a minute.');
    setResult(null);
    
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/api/upload-paper', {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.detail || 'Failed to process paper');
      }

      const data = await response.json();
      setResult(data);
      setStatus('Success! Project code generated.');
      
      // Set the first file as the active tab
      if (data.generated_code && Object.keys(data.generated_code).length > 0) {
        setActiveTab(Object.keys(data.generated_code)[0]);
      }
      
    } catch (error) {
      setStatus(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-5xl mx-auto mt-10">
      <div className="bg-white rounded-lg shadow-xl overflow-hidden mb-8">
        <div className="px-8 py-6">
          <h2 className="text-2xl font-bold mb-2 text-gray-800">Upload Research Paper</h2>
          <p className="text-gray-600 mb-6">Upload a PDF paper to extract hyperparameters and generate a PyTorch starter project.</p>
          
          <form onSubmit={handleUpload} className="flex items-end gap-4">
            <div className="flex-1">
              <label className="block text-gray-700 text-sm font-semibold mb-2" htmlFor="paper">
                Select PDF File
              </label>
              <input 
                type="file" 
                id="paper" 
                accept=".pdf"
                onChange={handleFileChange}
                className="w-full px-4 py-2 border border-gray-300 rounded-md text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors"
                disabled={loading}
              />
            </div>
            <button 
              type="submit"
              disabled={loading}
              className={`bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 px-6 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors ${loading ? 'opacity-70 cursor-not-allowed' : ''}`}
            >
              {loading ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Processing...
                </span>
              ) : 'Generate Code'}
            </button>
          </form>
          
          {status && (
            <div className={`mt-6 p-4 rounded-md text-sm font-medium ${status.startsWith('Error') ? 'bg-red-50 text-red-700' : 'bg-blue-50 text-blue-700'}`}>
              {status}
            </div>
          )}
        </div>
      </div>

      {result && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 pb-12">
          
          {/* Extracted Details Sidebar */}
          <div className="bg-white rounded-lg shadow-xl overflow-hidden lg:col-span-1 h-fit">
            <div className="bg-gray-50 px-6 py-4 border-b border-gray-200">
              <h3 className="text-lg font-bold text-gray-800">Extracted Details</h3>
            </div>
            <div className="p-6">
              <div className="space-y-4">
                {result.extracted_details && Object.entries(result.extracted_details).map(([key, value]) => {
                  // Format key nicely (e.g., learning_rate -> Learning Rate)
                  const formattedKey = key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
                  return (
                    <div key={key}>
                      <span className="block text-xs font-semibold text-gray-500 uppercase tracking-wider">{formattedKey}</span>
                      <span className="block mt-1 text-sm text-gray-900">{String(value)}</span>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Generated Code Section */}
          <div className="bg-white rounded-lg shadow-xl overflow-hidden lg:col-span-2">
            <div className="bg-gray-800 px-2 pt-2 flex flex-wrap gap-1">
              {result.generated_code && Object.keys(result.generated_code).map((filename) => (
                <button
                  key={filename}
                  onClick={() => setActiveTab(filename)}
                  className={`px-4 py-2 text-sm font-medium rounded-t-lg transition-colors ${activeTab === filename ? 'bg-gray-900 text-blue-400' : 'bg-gray-800 text-gray-400 hover:text-gray-200 hover:bg-gray-700'}`}
                >
                  {filename}
                </button>
              ))}
            </div>
            <div className="bg-gray-900 p-6 overflow-x-auto">
              <pre className="text-gray-300 text-sm font-mono whitespace-pre-wrap">
                {result.generated_code && result.generated_code[activeTab]}
              </pre>
            </div>
          </div>
          
        </div>
      )}
    </div>
  );
}

export default UploadForm;
