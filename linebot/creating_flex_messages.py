import datetime


class creating_flex_messages():
    def CreateFormAllStatusForMGR(dt, VIS_SUM_OFFLINE, MWGT_SUM_OFFLINE, NOZZLE_OFFLINE, BATTERY_OFFLINE, TOTAL_SITE_ACTIVE):
        data = {"type": "flex",
                "altText": "Flex Message",
                "contents":
                {
                    "type": "carousel",
                    "contents": [{
                        "type": "bubble",
                        "size": "mega",
                        "hero": {
                            "type": "image",
                            "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                            "align": "center",
                            "gravity": "bottom",
                            "size": "full",
                            "aspectRatio": "35:8",
                            "aspectMode": "fit",
                            "action": {
                                "type": "uri",
                                "label": "Line",
                                "uri": "https://linecorp.com/"
                            },
                            "position": "relative"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "VIS MONITOR STATUS",
                                    "weight": "bold",
                                    "size": "sm",
                                    "color": "#225508FF",
                                    "align": "center",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": str(dt),
                                    "weight": "bold",
                                    "size": "sm",
                                    "color": "#225508FF",
                                    "align": "center",
                                    "contents": []
                                },
                                {
                                    "type": "separator",
                                    "margin": "sm",
                                    "color": "#165C3CFF"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "margin": "lg",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Status",
                                            "weight": "bold",
                                            "size": "xs",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "VIS",
                                            "weight": "bold",
                                            "size": "xs",
                                            "align": "center",
                                            "position": "relative",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "MWGT",
                                            "weight": "bold",
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "Nozzle",
                                            "weight": "bold",
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "Battery",
                                            "weight": "bold",
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "margin": "md",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Offline",
                                            "size": "xs",
                                            "align": "start",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(VIS_SUM_OFFLINE),
                                            "size": "xs",
                                            "align": "center",
                                            "position": "relative",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(MWGT_SUM_OFFLINE),
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(NOZZLE_OFFLINE),
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": '-',
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "margin": "md",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Low:Volt",
                                            "size": "xs",
                                            "align": "start",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "-",
                                            "size": "xs",
                                            "align": "center",
                                            "position": "relative",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "-",
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "-",
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(BATTERY_OFFLINE),
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        }
                                    ]
                                },
                                {
                                    "type": "separator",
                                    "margin": "md",
                                    "color": "#165C3CFF"
                                },
                                {
                                    "type": "text",
                                    "text": "Total Online " + str(TOTAL_SITE_ACTIVE) + " Station",
                                    "weight": "bold",
                                    "size": "sm",
                                    "color": "#225508FF",
                                    "align": "center",
                                    "margin": "xxl",
                                    "contents": []
                                }
                            ]
                        }
                    }

                    ]

                }}
        return data
    
    def CreateFormVisFlexMessageDetail(data,user_type):
        if user_type.user_type.id == 6 :
            content_tech = {
                                        "type": "text",
                                        "text": 'ทีมงาน : ' + str(data['user_type'].if_technician.team) + ' คุณ : ' + str(data['user_type'].if_technician.team_name),
                                        "weight": "bold",
                                        "align": "center",
                                        "margin": "xs",
                                        "contents": []
                                    }
        if user_type.user_type.id != 6 :
            content_tech = {
                                        "type": "text",
                                        "text": '-',
                                        "weight": "bold",
                                        "align": "center",
                                        "margin": "xs",
                                        "contents": []
                                    }
            
        content = {
            "type": "carousel",
            "contents": [
                # ชุดที่ 1
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "VIS : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดสถานะ",
                                        "weight": "bold",
                                        "size": "lg",
                                        "align": "center",
                                        "gravity": "center",
                                        "contents": []
                                    },
                                    content_tech,
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Deive",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "gravity": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "OnLine",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "OffLine",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "VIS",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": str(int(data['TOTAL_SITE_ACTIVE']) - int(data['VIS_SUM_OFFLINE'])),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": str(data['VIS_SUM_OFFLINE']),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "Total Online " + str(data['TOTAL_SITE_ACTIVE']) + ' ' + " Station",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "margin": "xxl",
                                "contents": []
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "www.orpak.com",
                                    "uri": "https://www.orpak.com/"
                                },
                                "color": "#078025FF",
                                "margin": "none",
                                "height": "sm",
                                "style": "secondary"
                            },
                            {
                                "type": "spacer",
                                "size": "sm"
                            }
                        ]
                    }
                },
                # ชุดที่ 2
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "VIS : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ VIS Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "IP-Address",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงรายละเอียดสถานี
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                },
                # ชุดที่ 3
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "VIS : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ VIS Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "LastConnect",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงข้อมูลสถานี


                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                },
                # ชุดที่ 4
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "VIS : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "27-12-2020 20:18",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ VIS Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "LostTime",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงข้อมูล

                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                }
            ]
        }
        # ส่วนแสดงที่ loop 1
        if len(data['VIS_DETAIL']) <= 0:
            content_1 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][1]['body']['contents'].insert(-2, content_1)
        elif len(data['VIS_DETAIL']) > 0:
            for ip_address in data['VIS_DETAIL']:
                content_1 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['ip_address']),
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][1]['body']['contents'].insert(
                    -2, content_1)

        # ส่วนแสดงที่ loop 2
        if len(data['VIS_DETAIL']) <= 0:
            content_2 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][2]['body']['contents'].insert(-2, content_2)
        elif len(data['VIS_DETAIL']) > 0:
            for ip_address in data['VIS_DETAIL']:
                content_2 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['VIS_last_time'].strftime("%d.%m.%y %H:%M")),
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][2]['body']['contents'].insert(
                    -2, content_2)

        # ส่วนแสดงที่ loop 3
        if len(data['VIS_DETAIL']) <= 0:
            content_3 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][3]['body']['contents'].insert(-2, content_3)
        elif len(data['VIS_DETAIL']) > 0:
            for ip_address in data['VIS_DETAIL']:
                content_3 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['time_dif']['day']) + 'วัน' + str(ip_address['time_dif']['hour'])+'ชม.' + str(ip_address['time_dif']['minutes'])+'นาที',
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][3]['body']['contents'].insert(
                    -2, content_3)

        data = {"type": "flex",
                "altText": "Flex Message",
                "contents": content}
        return data
    
    def CreateFormMwgtFlexMessageDetail(data,user_type):
        if user_type.user_type.id == 6 :
            content_tech = {
                                        "type": "text",
                                        "text": 'ทีมงาน : ' + str(data['user_type'].if_technician.team) + ' คุณ : ' + str(data['user_type'].if_technician.team_name),
                                        "weight": "bold",
                                        "align": "center",
                                        "margin": "xs",
                                        "contents": []
                                    }
        if user_type.user_type.id != 6 :
            content_tech = {
                                        "type": "text",
                                        "text": '-',
                                        "weight": "bold",
                                        "align": "center",
                                        "margin": "xs",
                                        "contents": []
                                    }
        content = {
            "type": "carousel",
            "contents": [
                # ชุดที่ 1
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "MWGT : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดสถานะ",
                                        "weight": "bold",
                                        "size": "lg",
                                        "align": "center",
                                        "gravity": "center",
                                        "contents": []
                                    },
                                    content_tech,
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Deive",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "gravity": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "OnLine",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "OffLine",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "MWGT",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": str(int(data['TOTAL_SITE_ACTIVE']) - int(data['MWGT_SUM_OFFLINE'])),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": str(data['MWGT_SUM_OFFLINE']),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "Total Online " + str(data['TOTAL_SITE_ACTIVE']) + ' ' + " Station",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "margin": "xxl",
                                "contents": []
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "www.orpak.com",
                                    "uri": "https://www.orpak.com/"
                                },
                                "color": "#078025FF",
                                "margin": "none",
                                "height": "sm",
                                "style": "secondary"
                            },
                            {
                                "type": "spacer",
                                "size": "sm"
                            }
                        ]
                    }
                },
                # ชุดที่ 2
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "VIS : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ MWGT Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "Unit-Address",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงรายละเอียดสถานี
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                },
                # ชุดที่ 3
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "MWGT : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ MWGT Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "LastConnect",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงข้อมูลสถานี


                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                },
                # ชุดที่ 4
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "MWGT : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ MWGT Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "LostTime",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงข้อมูล

                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                }
            ]
        }
        # ส่วนแสดงที่ loop 1
        if len(data['MWTG_DETAIL']) <= 0:
            content_1 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][1]['body']['contents'].insert(-2, content_1)
        elif len(data['MWTG_DETAIL']) > 0:
            for ip_address in data['MWTG_DETAIL']:
                print (ip_address)
                content_1 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['DataUnitMap_IP']),
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][1]['body']['contents'].insert(
                    -2, content_1)

        # ส่วนแสดงที่ loop 2
        if len(data['MWTG_DETAIL']) <= 0:
            content_2 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][2]['body']['contents'].insert(-2, content_2)
        elif len(data['MWTG_DETAIL']) > 0:
            for ip_address in data['MWTG_DETAIL']:
                content_2 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['MWGT_last_time'].strftime("%d.%m.%y %H:%M")),
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][2]['body']['contents'].insert(
                    -2, content_2)

        # ส่วนแสดงที่ loop 3
        if len(data['MWTG_DETAIL']) <= 0:
            content_3 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][3]['body']['contents'].insert(-2, content_3)
        elif len(data['MWTG_DETAIL']) > 0:
            for ip_address in data['MWTG_DETAIL']:
                content_3 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['time_dif']['day']) + 'วัน' + str(ip_address['time_dif']['hour'])+'ชม.' + str(ip_address['time_dif']['minutes'])+'นาที',
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][3]['body']['contents'].insert(
                    -2, content_3)

        data = {"type": "flex",
                "altText": "Flex Message",
                "contents": content}
        return data
    
    def CreateFormNozzleFlexMessageDetail(data,user_type):
        if user_type.user_type.id == 6 :
            content_tech = {
                                        "type": "text",
                                        "text": 'ทีมงาน : ' + str(data['user_type'].if_technician.team) + ' คุณ : ' + str(data['user_type'].if_technician.team_name),
                                        "weight": "bold",
                                        "align": "center",
                                        "margin": "xs",
                                        "contents": []
                                    }
        if user_type.user_type.id != 6 :
            content_tech = {
                                        "type": "text",
                                        "text": '-',
                                        "weight": "bold",
                                        "align": "center",
                                        "margin": "xs",
                                        "contents": []
                                    }
        content = {
            "type": "carousel",
            "contents": [
                # ชุดที่ 1
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "NOZZLE : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดสถานะ",
                                        "weight": "bold",
                                        "size": "lg",
                                        "align": "center",
                                        "gravity": "center",
                                        "contents": []
                                    },
                                    content_tech,
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Deive",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "gravity": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "OnLine",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "OffLine",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NOZZLE",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": str(int(data['TOTAL_SITE_ACTIVE']) - int(data['NOZZLE_OFFLINE'])),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": str(data['NOZZLE_OFFLINE']),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "Total Online " + str(data['TOTAL_SITE_ACTIVE']) + ' ' + " Nozzle",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "margin": "xxl",
                                "contents": []
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "www.orpak.com",
                                    "uri": "https://www.orpak.com/"
                                },
                                "color": "#078025FF",
                                "margin": "none",
                                "height": "sm",
                                "style": "secondary"
                            },
                            {
                                "type": "spacer",
                                "size": "sm"
                            }
                        ]
                    }
                },
                # ชุดที่ 2
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "NOZZLE : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ NOZZLE Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "NozzleDetail",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงรายละเอียดสถานี
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                },
                # ชุดที่ 3
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "NOZZLE : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ NOZZLE Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "LastConnect",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงข้อมูลสถานี


                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                },
                # ชุดที่ 4
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/picture_logo/VIS-MONITOR/vis.png",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "35:8",
                        "aspectMode": "fit",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "NOZZLE : STATUS",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(data['TIME_UPDATE'].strftime("%d.%m.%Y %H:%M")),
                                "weight": "bold",
                                "size": "lg",
                                "color": "#225508FF",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "sm",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายละเอียดอุปกรณ์ NOZZLE Offline",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "xs",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานี",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "start",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "LostTime",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end",
                                        "contents": []
                                    }
                                ]
                            },
                            # ส่วนแสดงข้อมูล

                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#165C3CFF"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอีดดอื่น สามารถกดที่ ip address ที่ต้องการระบบจะจัดส่งรายละเอียดอื่นให้เพิ่มเติม",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#225508FF",
                                "align": "center",
                                "margin": "xxl",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                }
            ]
        }
        # ส่วนแสดงที่ loop 1
        if len(data['NOZZLE_DETAIL']) <= 0:
            content_1 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][1]['body']['contents'].insert(-2, content_1)
        elif len(data['NOZZLE_DETAIL']) > 0:
            for ip_address in data['NOZZLE_DETAIL']:
                print (ip_address)
                content_1 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str('Log : ' +ip_address['Unit_log_address'] + ' หน้า ' +ip_address['NOZZLE_pump_log_address'] + '/'+ip_address['NOZZLE_num']),
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][1]['body']['contents'].insert(
                    -2, content_1)

        # ส่วนแสดงที่ loop 2
        if len(data['NOZZLE_DETAIL']) <= 0:
            content_2 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][2]['body']['contents'].insert(-2, content_2)
        elif len(data['NOZZLE_DETAIL']) > 0:
            for ip_address in data['NOZZLE_DETAIL']:
                content_2 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['VIS_last_time'].strftime("%d.%m.%y %H:%M")),
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][2]['body']['contents'].insert(
                    -2, content_2)

        # ส่วนแสดงที่ loop 3
        if len(data['NOZZLE_DETAIL']) <= 0:
            content_3 = {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '-',
                        "weight": "bold",
                        "size": "xs",
                        "color": "#EC1019FF",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "text": "ไม่พบรายงาน",
                            "data": 'ไม่พบรายงาน'
                        },
                        "contents": []
                    }
                ]
            }
            content['contents'][3]['body']['contents'].insert(-2, content_3)
        elif len(data['NOZZLE_DETAIL']) > 0:
            for ip_address in data['NOZZLE_DETAIL']:
                content_3 = {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(ip_address['name']),
                            "weight": "bold",
                            "size": "xs",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(ip_address['time_dif']['day']) + 'วัน' + str(ip_address['time_dif']['hour'])+'ชม.' + str(ip_address['time_dif']['minutes'])+'นาที',
                            "weight": "bold",
                            "size": "xs",
                            "color": "#EC1019FF",
                            "align": "end",
                            "action": {
                                "type": "postback",
                                "text": "กำลังจัดส่งรายละเอียด",
                                "data": "check"+str(ip_address['ip_address'])
                            },
                            "contents": []
                        }
                    ]
                }
                content['contents'][3]['body']['contents'].insert(
                    -2, content_3)

        data = {"type": "flex",
                "altText": "Flex Message",
                "contents": content}
        return data