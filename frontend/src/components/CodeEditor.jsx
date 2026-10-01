export default function CodeEditor({ value, onChange, language = 'python' }) {
  return (
    <label className="editor-field">
      <span className="field-label">Source code <span>{language}</span></span>
      <textarea
        className="code-editor"
        spellCheck="false"
        value={value}
        onChange={(event) => onChange(event.target.value)}
        aria-label="Source code editor"
      />
    </label>
  );
}
