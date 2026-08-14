export interface MaintenanceRequest { id: string; status: 'OPEN' | 'ASSIGNED' | 'COMPLETED'; assigneeDisplayName: string; dueAt: string }
