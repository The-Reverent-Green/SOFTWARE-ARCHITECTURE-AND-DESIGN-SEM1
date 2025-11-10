from pystructurizr.dsl import Workspace

# Create the model
with Workspace() as workspace:
    with workspace.Model(name="model") as model:
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


