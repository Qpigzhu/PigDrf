# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\12\16 0016 20:48$'

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav,UserLeavingMessage
from goods.serializers import GoodsSerializers



class UserFavDetailSerializer(serializers.ModelSerializer):
    # 通过goods_id拿到商品信息。就需要嵌套的Serializer
        goods = GoodsSerializers()
        class Meta:
            model = UserFav
            fields = ("goods", "id")


class UserFavSerializers(serializers.ModelSerializer):
    #获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


    class Meta:
        model = UserFav
        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]
        fields = ("user","goods","id")


class UserLeavingMessageSerializers(serializers.ModelSerializer):
    #获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    #read_only自动获取时间，只读状态，不可写
    add_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("user","message_type","subject","message","file","add_time","id")