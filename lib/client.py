#
#   Copyright (c) 2019 One Identity
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
from msal import PublicClientApplication
from safeguard.sessions.plugin.logging import get_logger
from safeguard.sessions.plugin.plugin_configuration import PluginConfiguration

logger = get_logger(__name__)


class Client:
    def __init__(self, client_id, authority):
        self.app = PublicClientApplication(client_id=client_id, authority=authority)

    @classmethod
    def from_config(cls, plugin_configuration: PluginConfiguration):
        return cls(
            plugin_configuration.get("azure-ad", "client_id", required=True),
            plugin_configuration.get("azure-ad", "authority", default="https://login.microsoftonline.com/common")
        )

    def start_flow(self):
        return self.app.initiate_device_flow(["https://graph.microsoft.com/.default"])

    def poll_flow(self, flow):
        return self.app.acquire_token_by_device_flow(flow=flow)

    @staticmethod
    def is_flow_successful(result):
        return "access_token" in result
