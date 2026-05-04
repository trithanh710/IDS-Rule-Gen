from src.utils import format_msg


class SuricataGenerator:
    """
    Class dùng để sinh rule Suricata từ danh sách IP.
    SID sẽ tự động tăng bắt đầu từ 1000001.
    """

    def __init__(self, start_sid: int = 1000001):
        self.current_sid = start_sid

    def generate_rule(self, ip: str, description: str, sid: int) -> str:
        """
        Sinh một rule Suricata cho IP cụ thể.

        Args:
            ip (str): Địa chỉ IP
            description (str): Mô tả
            sid (int): Rule SID

        Returns:
            str: Rule hoàn chỉnh
        """

        clean_desc = format_msg(description)

        rule = (
            f"alert ip $EXTERNAL_NET {ip} -> $HOME_NET any "
            f"(msg:'Blacklisted IP: {clean_desc}'; sid:{sid}; rev:1;)"
        )

        return rule

    def generate_rules(self, entries: list) -> list:
        """
        Sinh nhiều rule từ danh sách input.

        Args:
            entries (list): [{"ip": "...", "description": "..."}]

        Returns:
            list[str]: Danh sách rule
        """

        rules = []

        for entry in entries:
            ip = entry.get("ip")
            desc = entry.get("description", "")

            rule = self.generate_rule(ip, desc, self.current_sid)
            rules.append(rule)

            self.current_sid += 1  # auto tăng SID

        return rules
