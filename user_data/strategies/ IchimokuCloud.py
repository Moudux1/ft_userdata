class IchimokuCloud(IStrategy):
    # Strategy interface version - allow new iterations of the strategy interface.
    # Check the documentation or the Sample strategy to get the latest version.
    INTERFACE_VERSION = 3
    # Optimal timeframe for the strategy.
    timeframe = '1h"
    # Can this strategy go short?
    can_short: bool = False
    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_ roi".
    minimal_roi = {
        "60":0.01,
        "30":0.02,
        "0":0.04
    }
    # Optimal stoploss designed for the strategy.
    # This attribute will be overridden if the config file contains "stoploss".
    stoploss = -0.10

    # Trailing stoploss
    trailing_stop = False
    # trailing_only_offset_is_reached = False
    # trailing_stop_positive = 0.01
    # trailing_stop_positive_offset = 0.0 # Disabled / not configured
    # Runt
    #ponulate indicatons(" onlv for new candle
    process_only_new_candles = True

    # These values can be overridden in the config-
    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = False
    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 250
    # Strategy parameters
    upper_cloud_multiplier = DecimalParameter(0.9, 1.1, decimals=2, default=1, space= 'buy')

    leverage_level = 1

    # Optional order type mapping.
    order_types = {
        'entry': 'limit',
        'exit': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }
    # Optional order time in force.
    order_time_in_force = {
        'entry': 'GTC',
        'exit': 'GTC'
    }

        
    @property

    def plot_config(self):

        return {

            # Main plot indicators (Moving averages,....)

            'main_plot': {

                'conversion_line': {'color': 'rgb(41, 98, 255)', 'style': 'line', 'width': 2},

                'base_line': {'color': 'rgb(183,28,28)', 'style': 'line', 'width': 2},

                # 'chikou_span': {'color': 'green', 'style': 'line', 'width': 2},

                'senkou_a': {

                    'color': 'rgb(165, 214, 167)', #optional

                    'fill_to': 'senkou_b',

                    'fill_label': 'Ichimoku Cloud', #optional

                    'fill_color': 'rgba(67, 160, 71, 0.1)', #optional

                },

                'senkou_b': {

                    'color': 'rgb(239, 154, 154)', #optional

                }

            }

        }
