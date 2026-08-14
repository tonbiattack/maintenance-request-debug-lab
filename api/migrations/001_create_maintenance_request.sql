create table maintenance_request (
  id uuid primary key,
  status varchar(16) not null check (status in ('OPEN', 'ASSIGNED', 'COMPLETED')),
  assignee_display_name varchar(120) not null,
  due_at timestamptz not null,
  version bigint not null default 0
);
