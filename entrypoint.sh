print_bold() {
    MESSAGE=$1; shift
    echo "\033[1;32m$MESSAGE\033[0m"
}

help_menu() {
   print_bold "Available Commands"
    echo ""
    echo "\033[1;34minstall\033[0m  Installs everithing. You should run this first"
    echo "run      Runs the example"
    echo ""
}

function file_exists() {
    FILE=$1; shift
    if [ -f "$FILE" ];
    then
        # File does exist
        return 0
    fi

    return 1
}

function install() {
    if ! file_exists "docker-compose.yml"
    then
        # Need to create docker-compose.yml
        echo "Creating docker-compose.yml"
        cp docker-compose.yml.example docker-compose.yml
    fi

    print_bold "Beginning instalation..."
    docker-compose build
    print_bold "Instalation finished succesfull"
}

function run() {
    return
}

COMMAND=$1; shift
case $COMMAND in
    install)
        install
    ;;
    run)
        docker-compose run app python main.py $@
    ;;
    *)
        help_menu
        echo "Invalid command $COMMAND";
        exit 1
    ;;
esac