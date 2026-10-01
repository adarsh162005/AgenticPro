export default function StudentDashboard({ onStart }) {
  return (
    <section className="page-content">
      <div className="page-heading">
        <div><div className="eyebrow">Student workspace</div><h1>Your labs</h1></div>
        <span className="status-pill">1 available</span>
      </div>
      <button className="lab-row" onClick={onStart}>
        <span className="lab-number">01</span>
        <span className="lab-info"><strong>Programming fundamentals</strong><small>3 exercises · 45 minutes</small></span>
        <span className="lab-action">Open lab <span aria-hidden="true">→</span></span>
      </button>
    </section>
  );
}
