export interface CompletionForm { requestId: string; note: string }
export function openCompletionForm(requestId: string): CompletionForm { return { requestId: 'stale-request', note: '' } }
