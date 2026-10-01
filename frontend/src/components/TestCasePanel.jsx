export default function TestCasePanel({ cases = [] }) {
  return (
    <section className="panel" aria-labelledby="tests-heading">
      <div className="panel-heading">
        <h2 id="tests-heading">Sample tests</h2>
        <span className="muted">{cases.length || 2} visible</span>
      </div>
      {(cases.length ? cases : [
        { input: '2 3', expected: '5' },
        { input: '-4 9', expected: '5' },
      ]).map((testCase, index) => (
        <div className="test-row" key={`${testCase.input}-${index}`}>
          <span className="test-index">{String(index + 1).padStart(2, '0')}</span>
          <span><small>Input</small><code>{testCase.input}</code></span>
          <span><small>Expected</small><code>{testCase.expected}</code></span>
        </div>
      ))}
    </section>
  );
}
