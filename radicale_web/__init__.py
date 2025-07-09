# This file is part of Radicale - CalDAV and CardDAV server
# Copyright © 2017-2018 Unrud <unrud@outlook.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Radicale.  If not, see <http://www.gnu.org/licenses/>.

"""
The web module for the website at ``/.web``.

Take a look at the class ``BaseWeb`` if you want to implement your own.

"""


from radicale import httputils, types, web
from http import client

MIMETYPES = httputils.MIMETYPES  # deprecated
FALLBACK_MIMETYPE = httputils.FALLBACK_MIMETYPE  # deprecated

class Web(web.BaseWeb):

    def get(self, environ: types.WSGIEnviron, base_prefix: str, path: str,user: str) -> types.WSGIResponse:
        if path == "/.web/get":
            headers = {"Content-Type": "text/plain"}
            answer = user
            return client.OK, headers, answer

        else:
            return httputils.serve_resource("radicale_web", "radicale_web_data",
                                        base_prefix, path)
