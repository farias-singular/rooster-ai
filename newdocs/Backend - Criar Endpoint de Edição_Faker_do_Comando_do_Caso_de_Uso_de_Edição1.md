```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public partial static class BrandHelper
    {
        private static Faker<UpdateBrandCommand> FakeUpdateBrandCommand(
            string? id = null,
            string? organizationId = null,
            Guid? categoryId = null,
            string? name = null,
            string? title = null)
        {
            return new Faker<UpdateBrandCommand>()
                .CustomInstantiator(f => new UpdateBrandCommand(
                    id ?? f.Random.String2(10),
                    organizationId ?? f.Random.String2(10),
                    categoryId ?? Guid.NewGuid(),
                    name ?? f.Company.CompanyName(),
                    title ?? f.Company.CompanySuffix()));
        }

        public static UpdateBrandCommand RandomUpdateBrandCommand(
            string? id = null,
            string? organizationId = null,
            Guid? categoryId = null,
            string? name = null,
            string? title = null)
        {
            return FakeUpdateBrandCommand(id, organizationId, categoryId, name, title).Generate();
        }
    }
}
```