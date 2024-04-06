if status is-interactive
    # Commands to run in interactive sessions can go here
end

set username (whoami)

function fish_greeting                                            
    set_color cyan; echo "Welcome back $username"
end