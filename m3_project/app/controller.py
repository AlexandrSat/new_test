from objectpack.observer import ObservableController, Observer

observer = Observer()
controller = ObservableController(url="/controller", observer=observer)
