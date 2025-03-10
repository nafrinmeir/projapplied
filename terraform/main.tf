provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "app_namespace" {
  metadata {
    name = "flask-app"
  }
}

resource "kubernetes_deployment" "flask_app" {
  metadata {
    name      = "flask-app"
    namespace = kubernetes_namespace.app_namespace.metadata[0].name
  }
  spec {
    replicas = 2
    selector {
      match_labels = {
        app = "flask-app"
      }
    }
    template {
      metadata {
        labels = {
          app = "flask-app"
        }
      }
      spec {
        container {
          image = "flask-app:latest"
          name  = "flask-container"
        }
      }
    }
  }
}
