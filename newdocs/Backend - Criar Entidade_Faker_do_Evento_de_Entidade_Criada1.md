```csharp
namespace Project.Tests.Domain.Common
{
    public static partial class EventFaker
    {
        private static Faker<BrandCreatedEvent> FakeBrandCreatedEvent(Brand? brand = null)
        {
            brand ??= EntityFaker.RandomBrand();

            return new Faker<BrandCreatedEvent>()
                .CustomInstantiator(_ => new BrandCreatedEvent(brand));
        }

        public static BrandCreatedEvent RandomBrandCreatedEvent(Brand? brand = null)
        {
            return FakeBrandCreatedEvent(brand).Generate();
        }
    }
}
```