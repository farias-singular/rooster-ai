```csharp
namespace Project.Tests.Domain.Common
{
    public static partial class EventFaker
    {
        private static Faker<BrandUpdatedEvent> FakeBrandUpdatedEvent(Brand? brand = null)
        {
            brand ??= EntityFaker.RandomBrand();

            return new Faker<BrandUpdatedEvent>()
                .CustomInstantiator(_ => new BrandUpdatedEvent(brand));
        }

        public static BrandUpdatedEvent RandomBrandUpdatedEvent(Brand? brand = null)
        {
            return FakeBrandUpdatedEvent(brand).Generate();
        }
    }
}
```