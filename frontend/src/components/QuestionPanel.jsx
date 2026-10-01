export default function QuestionPanel({ question }) {
  return (
    <section className="panel question-panel" aria-labelledby="question-heading">
      <div className="eyebrow">Current exercise</div>
      <h2 id="question-heading">{question?.title ?? 'Add two numbers'}</h2>
      <p>{question?.prompt ?? 'Read two integers from standard input and print their sum.'}</p>
      <div className="question-meta">
        <span>{question?.language ?? 'Python'}</span>
        <span>{question?.points ?? 10} points</span>
      </div>
    </section>
  );
}
