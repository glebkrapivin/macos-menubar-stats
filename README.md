![](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8%2C3.9-blue)
![](https://img.shields.io/badge/os-macOS-brightgreen)
# macos-menubar-stats
This set of scripts allows for easy creation of menu-bar apps, that collect and display custom data like exchange rates, air-quality and so on. 

[![image.png](https://i.postimg.cc/TY5M6syd/image.png)](https://postimg.cc/zVNPw0S6)

One can add custom sources by:
 - Inheriting from BaseProcessor class and overriding `get_data` method
 - Registering new processor with the app and providing `n_retries` and `period_sec` for retries and update intervals respectfully

```python
from processors import AirQualityProcessor
from menubar import App

a = App() \
    .register_processor(AirQualityProcessor(url='...')) \
    .run()
```


### TODO:
- [ ] Make that an installable package, delete optional dependencies from requirements
- [ ] Exponential backoff while retrying
- [ ] examples
