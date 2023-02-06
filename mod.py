import interactions
from interactions import Embed


def get_rules():
    rules = [
        "Respect the privacy and personal information of other members. Do not share any sensitive information without consent.",
        "No hate speech, harassment, bullying, or discrimination of any kind will be tolerated.",
        "Keep discussions and communication in a professional and respectful manner. Avoid using excessive profanity or making personal attacks.",
        "No spamming, excessive self-promotion, or disruptive behavior in any channels.",
        "Do not post any illegal or copyrighted material.",
        "Any form of cheating or exploiting in-game is strictly prohibited.",
        "Follow the specific guidelines for each channel. Stay on topic and avoid disrupting the purpose of the channel.",
        "Report any rule-breaking behavior to the moderators. Do not engage in any argument or conflict with another member.",
        "The moderators reserve the right to remove any content and take disciplinary action, including but not limited to banning and muting, as deemed necessary.",
        "Age Restriction: - StaRP is an 18+ community. By joining the server, you confirm that you are 18 years of age or older. Any members found to be under 18 years of age will be removed from the server.",
        "Everyone starts somewhere - Members should show patience and understanding towards new players and casual roleplayers. At the same time, all members must show respect for each other's play styles and not engage in behavior that intentionally disrupts the immersive experience for others.",
        "No metagaming - Members are prohibited from using information or knowledge obtained outside of the 'Verse to gain an upper hand."
    ]

    embed = Embed(title="StaRP Rules", color=0x00ff00)
    for i, rule in enumerate(rules, 1):
        rule_parts = rule.split(' - ')
        if len(rule_parts) == 2:
            embed.add_field(name=f"{i}. {rule_parts[0]}", value=rule_parts[1], inline=False)
        else:
            embed.add_field(name=f"{i}. {rule}", value="", inline=False)
    embed.set_footer(
        text="By joining the Discord server, you agree to abide by these rules and any changes made to them in the future. Failure to comply may result in disciplinary action.")
    return embed
