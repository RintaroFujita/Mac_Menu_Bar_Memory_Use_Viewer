import psutil
import rumps

@rumps.timer(1)
def dispTimer(sender):
    cpu = psutil.cpu_percent(interval=1)
    app.title = (f'CPU使用率:{cpu}%')
my_timer = rumps.Timer(dispTimer,1)
my_timer.start()


if __name__ == "__main__":
    app = rumps.App("CPU_USE", title='Under measurement...')
    cpu = psutil.cpu_percent(interval=1)


app.run()