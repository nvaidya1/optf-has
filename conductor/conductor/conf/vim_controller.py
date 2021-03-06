#
# -------------------------------------------------------------------------
#   Copyright (c) 2018 Intel Corporation Intellectual Property
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# -------------------------------------------------------------------------
#


from oslo_config import cfg

from conductor.i18n import _

VIM_CONTROLLER_EXT_MANAGER_OPTS = [
    cfg.ListOpt('extensions',
                default=['multicloud'],
                help=_('Extensions list to use')),
]


def register_extension_manager_opts(cfg=cfg.CONF):
    cfg.register_opts(VIM_CONTROLLER_EXT_MANAGER_OPTS, 'vim_controller')
