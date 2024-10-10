#!/bin/bash

DOCKER_CMD="docker compose -f docker-compose.yml"

generate_ignore_files() {
  # Ensure .commonignore exists
  if [ ! -f .commonignore ]; then
    echo "Error: .commonignore file not found"
    exit 1
  fi

  # Generate .gitignore
  echo "# Generated from .commonignore - do not edit directly" >.gitignore
  echo "" >>.gitignore
  cat .commonignore >>.gitignore
  echo "" >>.gitignore
  echo "# Git-specific ignore rules" >>.gitignore

  # Generate .dockerignore
  echo "# Generated from .commonignore - do not edit directly" >.dockerignore
  echo "" >>.dockerignore
  cat .commonignore >>.dockerignore
  echo "" >>.dockerignore
  echo "# Docker-specific ignore rules" >>.dockerignore
  echo "Dockerfile" >>.dockerignore
  echo "docker-compose.yml" >>.dockerignore
  echo "docker" >>.dockerignore
  echo ".gitignore" >>.dockerignore
}

generate_ignore_files

case "$1" in
start)
  $DOCKER_CMD up -d
  echo "Project started. Access it at http://localhost:3000"
  ;;
stop)
  $DOCKER_CMD down
  ;;
build)
  $DOCKER_CMD build
  ;;
setup)
  $DOCKER_CMD build
  ;;
test)
  $DOCKER_CMD run --rm app npm test
  ;;
shell)
  $DOCKER_CMD run --rm app /bin/bash
  ;;
python)
  $DOCKER_CMD run --rm app python3
  ;;
pip)
  $DOCKER_CMD run --rm app pip3 "${@:2}"
  ;;
*)
  echo "Usage: $0 {start|stop|build|setup|test|shell|python|pip}"
  exit 1
  ;;
esac
