case $1 in
'up')
  sudo docker-compose up
  ;;
'upd')
  sudo docker-compose up -d
  ;;
'down')
  sudo docker-compose down
  ;;
'build')
  sudo docker-compose up --build
  ;;
esac