export default function FacultyDashboard() {
  return (
    <section className="page-content">
      <div className="page-heading"><div><div className="eyebrow">Course overview</div><h1>Faculty dashboard</h1></div></div>
      <div className="stats-grid">
        <div className="stat-block"><span>Active exams</span><strong>01</strong></div>
        <div className="stat-block"><span>Submissions</span><strong>24</strong></div>
        <div className="stat-block"><span>Awaiting review</span><strong>03</strong></div>
      </div>
      <div className="panel table-panel"><div className="panel-heading"><h2>Recent activity</h2><span className="muted">Latest submissions</span></div>
        <p className="muted">Connect the API to load course activity.</p>
      </div>
    </section>
  );
}
