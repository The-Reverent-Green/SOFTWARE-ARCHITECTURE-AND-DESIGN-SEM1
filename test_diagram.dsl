workspace {
  model {
    properties {
      "structurizr.groupSeparator" "/"
    }
    user = Person "User" "" {
    }
    cms = SoftwareSystem "CMS" "" {
      frontend = Container "Frontend" "" {
      }
      api = Container "API" "" {
      }
      database = Container "Database" "" {
      }
    }
    user -> frontend "Uses" ""
    frontend -> api "Calls" "HTTPS"
    api -> database "Reads/writes" "SQL"
  }
  views {
    container cms {
      description "Container diagram showing system components"
      include *
      autoLayout
    }
    styles {
      element "Element" {
        shape "RoundedBox"
      }
      element "Software System" {
        background "#1168bd"
        color "#ffffff"
      }
      element "Container" {
        background "#438dd5"
        color "#ffffff"
      }
      element "Component" {
        background "#85bbf0"
        color "#000000"
      }
      element "Person" {
        background "#08427b"
        color "#ffffff"
        shape "Person"
      }
      element "Infrastructure Node" {
        background "#ffffff"
      }
      element "database" {
        shape "Cylinder"
      }
    }
  }
}
