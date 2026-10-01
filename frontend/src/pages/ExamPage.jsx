import { useState } from 'react';
import CodeEditor from '../components/CodeEditor.jsx';
import QuestionPanel from '../components/QuestionPanel.jsx';
import ResultPanel from '../components/ResultPanel.jsx';
import TestCasePanel from '../components/TestCasePanel.jsx';

export default function ExamPage() {
  const [source, setSource] = useState('a, b = map(int, input().split())\nprint(a + b)');
  const [result, setResult] = useState(null);
  const [running, setRunning] = useState(false);

  async function submit() {
    setRunning(true);
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'}/submissions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id: crypto.randomUUID(), exam_id: 'demo', question_id: 'sum', student_id: 'student-demo',
          language: 'python', source_code: source,
        }),
      });
      if (!response.ok) throw new Error('Submission could not be sent');
      setResult({ score: 0, feedback: 'Submission received. Evaluation status is available from the API.' });
    } catch (error) {
      setResult({ score: 0, feedback: error.message });
    } finally {
      setRunning(false);
    }
  }

  return (
    <section className="page-content exam-layout">
      <div className="page-heading">
        <div><div className="eyebrow">Programming fundamentals</div><h1>Exercise 01</h1></div>
        <span className="timer">45:00</span>
      </div>
      <div className="exam-grid">
        <div className="exam-sidebar"><QuestionPanel /><TestCasePanel /></div>
        <div className="editor-column">
          <CodeEditor value={source} onChange={setSource} />
          <div className="editor-actions">
            <span className="muted">Python 3.12</span>
            <button className="primary-button" onClick={submit} disabled={running}>
              {running ? 'Submitting…' : 'Submit solution'}
            </button>
          </div>
          <ResultPanel result={result} />
        </div>
      </div>
    </section>
  );
}
