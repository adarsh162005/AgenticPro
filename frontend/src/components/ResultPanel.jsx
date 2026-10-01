export default function ResultPanel({ result }) {
  if (!result) {
    return <div className="result-empty" role="status">Run your solution to see evaluation results.</div>;
  }
  return (
    <section className="result-panel" aria-live="polite">
      <div>
        <div className="eyebrow">Evaluation</div>
        <strong>{result.score ?? 0} points</strong>
      </div>
      <span className="result-feedback">{result.feedback ?? result.message ?? 'Evaluation complete.'}</span>
    </section>
  );
}
