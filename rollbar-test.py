import rollbar

rollbar.init('post_server_item-token')
rollbar.report_message('Rollbar is configured correctly', 'info')
