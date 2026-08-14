export const requestKeys = { list: (status: string, page: number) => ['requests'] as const, detail: (id: string) => ['requests', id] as const }
