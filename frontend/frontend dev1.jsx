import React, { useState } from "react";

export default function ScanAndValidate() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [name, setName] = useState("");
  const [source, setSource] = useState("");
  const [batchId, setBatchId] = useState("");
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState(null);

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

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    // Fake AI response after 2 seconds
    setTimeout(() => {
      setReport({
        status: "✅ Pure Herb Detected",
        compounds: ["Eugenol", "Beta-caryophyllene"],
        safety: "Safe for medicinal use",
      });
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-green-100 to-green-300 p-6">
      <h1 className="text-3xl font-bold text-green-800 mb-6">
        Herbchain Chemical AI
      </h1>

      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-xl rounded-2xl p-6 w-full max-w-lg space-y-4"
      >
        {/* Upload Herb Image */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Upload Herb Image
          </label>
          <input
            type="file"
            accept="image/*"
            onChange={onFileChange}
            className="block w-full border border-gray-300 rounded-lg p-2"
          />
          {preview && (
            <img
              src={preview}
              alt="Herb Preview"
              className="mt-3 rounded-lg shadow-md max-h-48 mx-auto"
            />
          )}
        </div>

        {/* Herb Details */}
        <input
          type="text"
          placeholder="Herb Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full border border-gray-300 rounded-lg p-2"
          required
        />
        <input
          type="text"
          placeholder="Source"
          value={source}
          onChange={(e) => setSource(e.target.value)}
          className="w-full border border-gray-300 rounded-lg p-2"
        />
        <input
          type="text"
          placeholder="Batch ID"
          value={batchId}
          onChange={(e) => setBatchId(e.target.value)}
          className="w-full border border-gray-300 rounded-lg p-2"
        />

        {/* Scan Button */}
        <button
          type="submit"
          disabled={loading}
          className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded-lg font-semibold transition"
        >
          {loading ? "Scanning..." : "Scan & Validate"}
        </button>
      </form>

      {/* Report Section */}
      {report && (
        <div className="mt-6 bg-white shadow-lg rounded-2xl p-6 w-full max-w-lg">
          <h2 className="text-xl font-bold text-green-700 mb-2">
            Chemical Report
          </h2>
          <p className="text-gray-700">{report.status}</p>
          <p className="text-gray-700">
            <strong>Active Compounds:</strong> {report.compounds.join(", ")}
          </p>
          <p className="text-gray-700">
            <strong>Safety Status:</strong> {report.safety}
          </p>
        </div>
      )}
    </div>
  );
}
