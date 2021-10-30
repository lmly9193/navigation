<?php

unlink('webstack.md');

$groups = json_decode(file_get_contents('webstack.json'));

function save($content)
{
    file_put_contents('webstack.md', $content, FILE_APPEND | LOCK_EX);
}

foreach ($groups as $group) {
    save("## $group->taxonomy\n\n");
    if (!empty($group->links)) {
        save("|網站|說明|\n");
        save("|--|--|\n");
        foreach ($group->links as $site) {
            $description = $site->description ?? '';
            save("|[$site->title]($site->url)|$description|\n");
        }
        save("\n");
    }

    if (!empty($group->list)) {
        foreach ($group->list as $terms) {
            save("### $terms->term\n\n");
            save("|網站|說明|\n");
            save("|--|--|\n");
            foreach ($terms->links as $site) {
                $description = $site->description ?? '';
                save("|[$site->title]($site->url)|$description|\n");
            }
            save("\n");
        }
    }
}
