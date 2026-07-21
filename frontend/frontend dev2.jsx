import React, { useState } from "react";

export default function HerbAnalysis() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const onFileChange = (e) => {
    const f = e.target.files[0];
    setFile(f);
    if (f) {
      const url = URL.createObjectURL(f);
      setPreview(url);
    } else {
      setPreview(null);
    }
  };

  const analyzeHerb = () => {
    setLoading(true);
    setTimeout(() => {
      setResult({
        purity: "90%",
        adulterants: "None detected",
        recommended: "Suitable for Ayurvedic medicine",
      });
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-green-50 flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold text-green-800 mb-6">
        Herbchain - AI Herb Analysis
      </h1>

      <div className="bg-white shadow-lg rounded-2xl p-6 w-full max-w-md space-y-4">
        <input
          type="file"
          accept="image/*"
          onChange={onFileChange}
          className="block w-full border border-gray-300 rounded-lg p-2"
        />

        {preview && (
          <img
            src={preview}
            alt="Preview"
            className="rounded-lg shadow-md max-h-60 mx-auto"
          />
        )}

        <button
          onClick={analyzeHerb}
          disabled={loading}
          className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded-lg font-semibold transition"
        >
          {loading ? "Analyzing..." : "Generate Report"}
        </button>
      </div>

      {result && (
        <div className="mt-6 bg-white shadow-md rounded-2xl p-6 w-full max-w-md">
          <h2 className="text-lg font-bold text-green-700 mb-2">
            Herb Report
          </h2>
          <p>Purity: {result.purity}</p>
          <p>Adulterants: {result.adulterants}</p>
          <p>Recommendation: {result.recommended}</p>
        </div>
      )}
    </div>
  );
}
