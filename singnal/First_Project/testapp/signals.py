from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


# This Will call When user login successfully.
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print()
    print('*'*30, 'Login Successfully', 30*'*')
    print()
    print('logged in singnal ... Run Intro')
    print('sender:', sender)
    print('Rquest:',request)
    print('User:', user)
    print('User Password:',user.password)
    print(f'kwargs: {kwargs}')
    print()
# user_logged_in.connect(login_success, sender=User) #We can use this instead of decorator @reversed(user_logged_in, sender=User)

# This will call when user logedin 
@receiver(user_logged_out, sender=User)
def loguot_success(sender, request, user, **kwargs):
    print()
    print('*'*30, 'Loged Out Successfully', 30*'*')
    print()
    print('logedout in signal...Run Intro')
    print('sender', sender)
    print('Request:',request)
    print('user:',user)
    print('user password:', user.password)
    print(f'kwargs: {kwargs}')
    print()
# user_logged_out.connect(loguot_success, sender=User) #We can use this instead of decorator @receiver(user_logged_out, sender=User)

# This will call when user login failed, Thats means given credentials were worong!!!!
# Login and Logout singnals
@receiver(user_login_failed)
def login_failded(sender, credentials, request, **kwargs):
    print()
    print('*'*30, 'Login Failed', 30*'*')
    print()
    print('logedin Failled signal...Run Intro')
    print('sender', sender)
    print('Request:',request)
    print('credentials:',credentials)
    print(f'kwargs: {kwargs}')
    print()
# user_login_failed.connect(login_failded) #We can use this instead of decorator @receiver(user_login_failed)


# Model Signals
@receiver(pre_save, sender=User)
def at_ending_save(sender, instance, **kwargs):
    print()
    print('*'*30, 'Before Saving Data', 30*'*')
    print()
    print('sender:',sender)
    print('instance:',instance)
    print(f'kwargs: {kwargs}')
    print()

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print()
        print('*'*30, 'Created New Data', 30*'*')
        print()
        print('New Record')
        print('Sender:',sender)
        print('Instance:', instance)
        print(f'kwargs: {kwargs}')
        print()

    else:
        print()
        print('*'*30, 'Updating Existing Data', 30*'*')
        print()
        print('post save signal')
        print('User Updated')
        print('sender:',sender)
        print('instance:',instance)
        print('created:',created)
        print(f'kwargs: {kwargs}')
        print()



@receiver(pre_delete, sender=User)
def at_begging_delete(sender, instance, **kwargs):
    print()
    print('*'*30, 'Before Deleting Data', 30*'*')
    print()
    print('At Beginninng (pre_delete)')
    print('Sender:',sender)
    print('instance:',instance)
    print(f'kwargs: {kwargs}')
    print()


@receiver(post_delete, sender=User)
def at_end_deleting(sender, instance, **kwargs):
    print()
    print('*'*30, 'After Deleting Data', 30*'*')
    print()
    print('At Ending Delete (post deleting)')
    print('Sender:',sender)
    print('instance:',instance)
    print(f'kwargs: {kwargs}')
    print()


@receiver(pre_init, sender=User)
def at_begeinning_init(sender, *args, **kwargs):
    print('==================================')
    print('Pre init signal')
    print('sender:',sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print()


@receiver(post_init, sender=User)
def at_ending_init(sender,*args,**kwargs):
    print('===================================')
    print('post init signal')
    print('sender:',sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print()


# Request/Response Signals
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print()
    print('*'*30, 'Before Rquest processing', 30*'*')
    print()
    print('At Beginning Request')
    print('Sender:',sender)
    print('environ:',environ)
    print(f'kwargs: {kwargs}')
    print()


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print()
    print('*'*30, 'After Rquest processing', 30*'*')
    print()
    print('At End Request')
    print('Sender:',sender)
    print(f'kwargs: {kwargs}')
    print()


@receiver(got_request_exception)
def at_ending_request(sender, request, **kwargs):
    print()
    print('*'*30, 'Some Exception Error!', 30*'*')
    print()
    print('At got request Exceptions')
    print('Sender:',sender)
    print('environ:',request)
    print(f'kwargs: {kwargs}')
    print()

    

# Management Singnals
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print()
    print('*'*30, 'Pre Migrate Signal', 30*'*')
    print()
    print('Sender:',sender)
    print('app_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('using:', using)
    print('plan:',plan)
    print('apps:',apps)
    print(f'kwargs: {kwargs}')
    print()


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print()
    print('*'*30, 'Post Migrate Signal', 30*'*')
    print()
    print('Sender:',sender)
    print('app_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('using:', using)
    print('plan:',plan)
    print('apps:',apps)
    print(f'kwargs: {kwargs}')
    print()



# Database Wrapper
@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print()
    print('*'*30, 'Database Connection Created!!', 30*'*')
    print()
    print('Initial Database Connections!!!')
    print(f'sender: {sender}')
    print(f'Connection: {connection}')
    print(f'Kwargs {kwargs}')
    print()
