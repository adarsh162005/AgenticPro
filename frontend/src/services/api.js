const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api';

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });
  if (!response.ok) {
    throw new Error(`API request failed (${response.status})`);
  }
  return response.json();
}

export const api = {
  getExam: (id) => request(`/exams/${id}`),
  getQuestion: (id) => request(`/questions/${id}`),
  submit: (submission) => request('/submissions', {
    method: 'POST',
    body: JSON.stringify(submission),
  }),
  getEvaluation: (submissionId) => request(`/evaluations/${submissionId}`),
};
