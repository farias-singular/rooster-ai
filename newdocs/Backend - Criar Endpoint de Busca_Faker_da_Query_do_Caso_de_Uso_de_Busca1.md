```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public partial static class BrandHelper
    {
        private static Faker<GetAllBrandsQuery> FakeGetAllBrandsQuery(
            string? brandIdOrName = null,
            IEnumerable<string>? brandIds = null,
            BrandOrderBy? orderBy = null,
            bool? orderByDescending = null,
            int? offset = null,
            int? limit = null)
        {
            return new Faker<GetAllBrandsQuery>()
                .CustomInstantiator(f => new GetAllBrandsQuery(
                    brandIdOrName ?? f.Random.String2(10),
                    brandIds ?? new List<string> { f.Random.String2(10) },
                    orderBy ?? BrandOrderBy.Name,
                    orderByDescending ?? f.Random.Bool(),
                    offset ?? f.Random.Int(0, 100),
                    limit ?? f.Random.Int(1, 100)));
        }

        public static GetAllBrandsQuery RandomGetAllBrandsQuery(
            string? brandIdOrName = null,
            IEnumerable<string>? brandIds = null,
            BrandOrderBy? orderBy = null,
            bool? orderByDescending = null,
            int? offset = null,
            int? limit = null)
        {
            return FakeGetAllBrandsQuery(brandIdOrName, brandIds, orderBy, orderByDescending, offset, limit).Generate();
        }
    }
}
```