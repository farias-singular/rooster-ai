```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public partial static class BrandHelper
    {
        private static Faker<CreateBrandCommand> FakeCreateBrandCommand(
            string? id = null,
            string? organizationId = null,
            Guid? categoryId = null,
            string? name = null,
            string? title = null)
        {
            return new Faker<CreateBrandCommand>()
                .CustomInstantiator(f => new CreateBrandCommand(
                    id ?? f.Random.String2(10),
                    organizationId ?? f.Random.String2(10),
                    categoryId ?? Guid.NewGuid(),
                    name ?? f.Company.CompanyName(),
                    title ?? f.Company.CompanySuffix()));
        }

        public static CreateBrandCommand RandomCreateBrandCommand(
            string? id = null,
            string? organizationId = null,
            Guid? categoryId = null,
            string? name = null,
            string? title = null)
        {
            return FakeCreateBrandCommand(id, organizationId, categoryId, name, title).Generate();
        }
    }
}
```