from rest_framework import serializers
from myweb.models import Registration
from wishlist.models import UserWishlist


# class WishlistSerializer(serializers.ModelSerializer):
#     registrations = serializers.PrimaryKeyRelatedField(queryset=Registration.objects.all(), many=True)

#     class Meta:
#         model = WishList
#         fields = ['id','user','registrations','created_at','updated_at']
#         read_only_fields = ['created_at','updated_at']
#         extra_kwargs = {'user': {'read_only': True}}

#     def create(self, validated_data):
#         user = self.context['request'].user
#         registrations = validated_data.pop('registrations',[])
#         wishlist,created = WishList.objects.get_or_create(user=user)
#         wishlist.registrations.set(registrations)
#         wishlist.save()
#         return wishlist
    

class UserWishlistSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='wishlist_registration.user_id.username', read_only=True)
    gender = serializers.CharField(source='wishlist_registration.gender', read_only=True)
    height = serializers.CharField(source='wishlist_registration.height', read_only=True)
    weight = serializers.CharField(source='wishlist_registration.weight', read_only=True)
    date_of_birth = serializers.CharField(source='wishlist_registration.date_of_birth', read_only=True)
    religious = serializers.CharField(source='wishlist_registration.religious', read_only=True)
    caste = serializers.CharField(source='wishlist_registration.caste', read_only=True)
    mother_tongue = serializers.CharField(source='wishlist_registration.mother_tongue', read_only=True)
    photo1 = serializers.CharField(source='wishlist_registration.photo1', read_only=True)
    educational_qualification = serializers.CharField(source='wishlist_registration.educational_qualification', read_only=True)
    state = serializers.CharField(source='wishlist_registration.state', read_only=True)
    district = serializers.CharField(source='wishlist_registration.district', read_only=True)
    marital_status = serializers.CharField(source='wishlist_registration.marital_status', read_only=True)
    job = serializers.CharField(source='wishlist_registration.job', read_only=True)

    class Meta:
        model = UserWishlist
        fields = ['id', 'wishlist_user', 'wishlist_registration', 'username', 'gender',
                  'height', 'weight', 'date_of_birth', 'religious', 'caste', 'mother_tongue', 'photo1',
                  'educational_qualification', 'state', 'district', 'marital_status', 'job']
        read_only_fields = ['wishlist_user']

    def create(self, validated_data):
        user = self.context['request'].user
        registration_id = validated_data.get('wishlist_registration')
        wishlist, created = UserWishlist.objects.get_or_create(
            wishlist_user=user,
            wishlist_registration=registration_id
        )
        return wishlist

