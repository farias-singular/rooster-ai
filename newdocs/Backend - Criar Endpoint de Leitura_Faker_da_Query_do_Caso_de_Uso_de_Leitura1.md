```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public partial static class BrandHelper
    {
        private static Faker<GetBrandByIdQuery> FakeGetBrandByIdQuery(
            string? id = null,
            string? organizationId = null)
        {
            return new Faker<GetBrandByIdQuery>()
                .CustomInstantiator(f => new GetBrandByIdQuery(
                    id ?? f.Random.String2(10),
                    organizationId ?? f.Random.String2(10)));
        }

        public static GetBrandByIdQuery RandomGetBrandByIdQuery(
            string? id = null,
            string? organizationId = null)
        {
            return FakeGetBrandByIdQuery(id, organizationId).Generate();
        }
    }
}
```