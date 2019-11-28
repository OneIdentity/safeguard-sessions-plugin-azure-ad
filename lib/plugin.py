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
from safeguard.sessions.plugin.aa_plugin import AAPlugin
from safeguard.sessions.plugin.plugin_base import cookie_property, lazy_property
from safeguard.sessions.plugin.plugin_response import AAResponse
from .client import Client


class Plugin(AAPlugin):
    def do_authenticate(self):
        result = self.azure_client.poll_flow(self.azure_device_flow)
        self.logger.debug("Device flow result: {}".format(result))
        if self.azure_client.is_flow_successful(result):
            return AAResponse.accept()
        else:
            return AAResponse.deny()

    def _ask_mfa_password(self):
        if self.mfa_password is not None:
            return None

        verification_uri = self.azure_device_flow.get("verification_uri")
        user_code = self.azure_device_flow.get("user_code")
        if not verification_uri or not user_code:
            return AAResponse.deny(reason="Could not acquire device flow from Microsoft Azure. See logs for details.")

        prompt = "Visit {} URL to sign in and use code {} to enable this connection. Press ENTER to continue.".format(
            verification_uri,
            user_code,
        )

        return AAResponse.need_info(
            question=prompt,
            key='otp',
            disable_echo=False
        )

    @lazy_property
    def azure_client(self):
        return Client.from_config(self.plugin_configuration)

    @cookie_property
    def azure_device_flow(self):
        flow = self.azure_client.start_flow()
        self.logger.debug("Device flow: {}".format(flow))
        return flow
