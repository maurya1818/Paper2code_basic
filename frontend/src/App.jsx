import React from 'react';
import UploadForm from './components/UploadForm';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
            Paper2Code
          </h1>
          <p className="mt-5 max-w-xl mx-auto text-xl text-gray-500">
            Automate the extraction of important implementation details from research papers and generate runnable project structures.
          </p>
        </div>
        
        <UploadForm />
      </div>
    </div>
  );
}

export default App;
