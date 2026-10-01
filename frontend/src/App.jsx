import { useState } from 'react';
import ExamPage from './pages/ExamPage.jsx';
import FacultyDashboard from './pages/FacultyDashboard.jsx';
import ResultsPage from './pages/ResultsPage.jsx';
import StudentDashboard from './pages/StudentDashboard.jsx';
import './styles.css';

const views = ['Labs', 'Faculty', 'Results'];

export default function App() {
  const [view, setView] = useState('Labs');
  const [inExam, setInExam] = useState(false);

  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="#home" onClick={(event) => { event.preventDefault(); setView('Labs'); setInExam(false); }}>
          <span className="brand-mark">PL</span><span>Programming Lab <small>ASSESSMENT</small></span>
        </a>
        <nav aria-label="Main navigation">
          {views.map((item) => <button key={item} className={view === item && !inExam ? 'nav-link active' : 'nav-link'} onClick={() => { setView(item); setInExam(false); }}>{item}</button>)}
        </nav>
        <button className="profile-button" aria-label="Signed in as student">JD</button>
      </header>
      <main>
        {inExam ? <ExamPage /> : view === 'Labs' ? <StudentDashboard onStart={() => setInExam(true)} /> : view === 'Faculty' ? <FacultyDashboard /> : <ResultsPage />}
      </main>
      <footer><span>Programming Lab Evaluation</span><span>Automated assessment workspace</span></footer>
    </div>
  );
}
