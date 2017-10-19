# Needs OctoPrint 1.3.6 or newer

def hook(apikey, *args, **kwargs):
	from octoprint.server import userManager
	return userManager.findUser(userid=apikey)

__plugin_hooks__ = {
	"octoprint.accesscontrol.keyvalidator": hook
}

