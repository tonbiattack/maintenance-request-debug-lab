export const requestKeys = { list: (status: string, page: number) => ['requests', status, page] as const, detail: (id: string) => ['requests', id] as const }
