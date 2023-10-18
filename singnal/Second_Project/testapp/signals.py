from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import pre_migrate, post_migrate
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

@receiver(pre_migrate)
def before_instal_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwars):
    print()
    print('*'*45,'Before Migrate',45*'*')
    print(f'sender: {sender}')
    print(f'app_config: {app_config}')
    print(f'verbosity: {verbosity}')
    print(f'interactive: {interactive}')
    print(f'using: {using}')
    print(f'plan: {plan}')
    print(f'kwargs: {kwars}')

@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print()
    print('*'*45,'After Migrate',45*'*')
    print(f'sender: {sender}')
    print(f'app_config: {app_config}')
    print(f'verbosity: {verbosity}')
    print(f'interactive: {interactive}')
    print(f'using: {using}')
    print(f'plan: {plan}')