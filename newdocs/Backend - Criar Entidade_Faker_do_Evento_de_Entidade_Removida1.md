```csharp
namespace Project.Tests.Domain.Common
{
    public static partial class EventFaker
    {
        private static Faker<BrandDeletedEvent> FakeBrandDeletedEvent(Brand? brand = null)
        {
            brand ??= EntityFaker.RandomBrand();

            return new Faker<BrandDeletedEvent>()
                .CustomInstantiator(_ => new BrandDeletedEvent(brand));
        }

        public static BrandDeletedEvent RandomBrandDeletedEvent(Brand? brand = null)
        {
            return FakeBrandDeletedEvent(brand).Generate();
        }
    }
}
```