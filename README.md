![](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8%2C3.9-blue)
![](https://img.shields.io/badge/os-macOS-brightgreen)
# macos-menubar-stats
This set of scripts allows for easy creation of menu-bar apps, that collect and display custom data like exchange rates, air-quality and so on. 

[![image.png](https://i.postimg.cc/YqfZLr5n/image.png)](https://postimg.cc/9r0JvhFZ)

One can add custom sources by:
 - Inheriting from BaseProcessor class and overriding `get_data` method
 - Registering new processor with the app and providing `n_retries` and `period_sec` for retries and update intervals respectfully

Another thing that came in handy is a possibility to register a new menu item callback to get a clickable button that, for instance, copies unique meeting id to clipboard

```python
from processors import AirQualityProcessor
from menu_callbacks import MeetzoneMenuItem
from menubar import App

a = App() \
    .register_processor(AirQualityProcessor(url='...')) \
    .register_menu_callback(MeetzoneMenuItem()) \
    .run()
```


### TODO:
- [X] Implement registering custom menu callbacks
- [ ] Make that an installable package, delete optional dependencies from requirements
- [ ] Exponential backoff while retrying
- [ ] examples
