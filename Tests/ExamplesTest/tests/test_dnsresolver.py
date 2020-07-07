import pytest
from test_utils import ExampleTest

@pytest.mark.dnsresolver
class TestDNSResolver(ExampleTest):

	def test_sanity(self):
		args = {
			'-s': 'www.google.com',
		}
		completed_process = self.run_example(args=args, requires_root=True)
		assert 'IP address of [www.google.com] is:' in completed_process.stdout

	def test_hostname_not_provided(self):
		args = {}
		completed_process = self.run_example(args=args, expected_return_code=1)
		assert 'Error: Hostname not provided' in completed_process.stdout

	def test_hostname_not_exist(self):
		args = {
			'-s': 'www.dlgkdflgkjdfkl.com',
			'-t': '1'
		}
		completed_process = self.run_example(args=args, requires_root=True)
		assert 'Could not resolve hostname' in completed_process.stdout

	@pytest.mark.interface_needed
	def test_use_specific_interface(self, interface_to_use):
		assert interface_to_use is not None
		args = {
			'-s': 'www.google.com',
			'-i': interface_to_use,
		}
		completed_process = self.run_example(args=args, requires_root=True)
		assert 'IP address of [www.google.com] is:' in completed_process.stdout