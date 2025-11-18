'''
This file is used to model the C4 models.
'''
from pystructurizr.dsl import Workspace

'''bash cmds
pystructurizr dump --view this_filename > output.dsl
pystructurizr dump --view C4_models > CMS_Context.dsl
'''
#Context C4 Level 1
with Workspace() as workspace:
    with workspace.Model(name="Context") as model:
        #Define the users
        consumer = model.Person("Consumer")
        agent = model.Person("Help Desk Agent")
        manager = model.Person("Help desk Manager")
        supporter = model.Person("Support Agent")
        sysAd = model.Person("System Administrator")

        with model.SoftwareSystem("CMS") as software_system:
            webapp = software_system.Container("Frontend")
            api = software_system.Container("API")
            db = software_system.Container("Database")
        
        consumer.uses(webapp, "Uses")
        webapp.uses(api, "Calls", "HTTPS")
        api.uses(db, "Reads/writes", "SQL")
    
    workspace.ContainerView(
        software_system,
        "Container View",
        "Container diagram showing system components"
    )