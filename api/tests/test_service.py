import unittest
from datetime import datetime, timezone
from app.service import *
class MaintenanceContractsTest(unittest.TestCase):
  def test_m01_validation_is_not_success(self): self.assertEqual(error_status(ValidationProblem('bad')), 400)
  def test_m03_stable_ordering_exists(self): self.assertIn('order by due_at asc, id asc', stable_list_sql('OPEN', 1))
  def test_m05_utc_conversion(self): self.assertEqual(normalize_due_at(datetime.now(timezone.utc)).tzinfo, timezone.utc)
  def test_m06_batch_query(self): self.assertIn('in (?, ?, ?)', batch_assignee_sql(3))
  def test_m07_atomic_completion(self): self.assertFalse(atomic_completion(True, False))
  def test_m08_status_constraint_contract(self): self.assertFalse(valid_status('UNKNOWN'))
  def test_m09_required_assignee(self):
    with self.assertRaises(ValueError): required_assignee_display_name('')
  def test_m10_request_id_exists(self): self.assertTrue(request_id_for_log(None))
  def test_m04_version_exists(self): self.assertEqual(MaintenanceRequest('r', 'OPEN', 'A', datetime.now(timezone.utc)).version, 0)
if __name__ == '__main__': unittest.main()
