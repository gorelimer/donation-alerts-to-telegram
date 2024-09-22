import aiogram
from donation_alerts_handler import donation_alerts
from donation_alerts_handler.types import donations

from .utils import form_render


ALERT_TEMPLATE_PATH: str = "src\\templates\\alert_message_body.jinja"


class TelegramAlertsHandler(donation_alerts.Client):
    telegram_bot: aiogram.Bot

    def __init__(
        self,
        bot: aiogram.Bot,
        chat_id: int,
        widget_token: str
    ) -> None:
        super().__init__(token=widget_token)
        self.chat_id = chat_id
        self.telegram_bot = bot
        self.filters = tuple()
        self.handlers.update({self.donate_handler: self.filters})

    async def donate_handler(self, donate: donations.Donations):
        text = await form_render(ALERT_TEMPLATE_PATH, donate=donate)
        await self.telegram_bot.send_message(
            chat_id=self.chat_id,
            text=text
        )
